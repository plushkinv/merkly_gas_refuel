import json
import time
from web3 import Web3
from eth_abi import encode
import requests
import random
from datetime import datetime
import config
import fun
from fun import log, save_wallet_to


network_from = "arbitrum" # arbitrum / polygon / optimism / bsc / fantom / avax / 
network_to = "kava" # arbitrum / polygon / optimism / bsc / fantom / avax / harmony / celo / moonbeam / fuse / gnosis / klaytn / metis / coredao / okt / zkevm / canto / zksyncera / moonriver / tenet / nova / meter / kava
amount = 0.0001 #указываете сколько хотите получить нативного токена в сети назначения


current_datetime = datetime.now()
print(f"\n\n {current_datetime}")
print(f'============================================= Плюшкин Блог =============================================')
print(f'subscribe to : https://t.me/plushkin_blog \n============================================================================================================\n')


keys_list = []
with open("private_keys.txt", "r") as f:
    for row in f:
        private_key=row.strip()
        if private_key:
            keys_list.append(private_key)

random.shuffle(keys_list)
i=0
for private_key in keys_list:
    i+=1
    if config.proxy_use == 2:
        while True:
            try:
                requests.get(url=config.proxy_changeIPlink)
                fun.timeOut("teh")            
                result = requests.get(url="https://yadreno.com/checkip/", proxies=config.proxies)
                print(f'Ваш новый IP-адрес: {result.text}')
                break
            except Exception as error:
                print(' !!! Не смог подключиться через Proxy, повторяем через 2 минуты... ! Чтобы остановить программу нажмите CTRL+C или закройте терминал')
                time.sleep(120)



    
    try:
        web3 = Web3(Web3.HTTPProvider(fun.address[network_from]["rpc"]))
        account = web3.eth.account.from_key(private_key)
        wallet = account.address    
        log(f"I-{i}: Начинаю работу с {wallet}")

        dapp_abi = json.load(open('abi/brige_abi.json'))
        dapp_address = web3.to_checksum_address(fun.address[network_from]["merkly_gas_refuel"])
        dapp_contract = web3.eth.contract(address=dapp_address, abi=dapp_abi)  

        amount_wei = web3.to_hex(encode(["uint"],[web3.to_wei(amount , "ether")]
            ))

        params = "0x0002000000000000000000000000000000000000000000000000000000000003d090"+amount_wei[2:]+wallet[2:]

        fees = dapp_contract.functions.estimateGasBridgeFee(
                fun.address[network_to]['lzChainId'],
                False,
                params
            ).call()

        fee= fees[0]

        gasPrice = web3.eth.gas_price
        transaction = dapp_contract.functions.bridgeGas(
                fun.address[network_to]['lzChainId'],  
                "0x0000000000000000000000000000000000000000",
                params,
            ).build_transaction({
            'from': wallet,
            'value': fee,
            'gasPrice': gasPrice,
            'nonce': web3.eth.get_transaction_count(wallet),
        })
        gasLimit = web3.eth.estimate_gas(transaction)
        transaction['gas'] = int(gasLimit * config.gas_kef)


        # Подписываем и отправляем транзакцию
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = web3.to_hex(web3.eth.send_raw_transaction(signed_txn.rawTransaction))
        tx_result = web3.eth.wait_for_transaction_receipt(tx_hash)

        if tx_result['status'] == 1:
            fun.log_ok(f'bridge OK: {tx_hash}')
        else:
            fun.log_error(f'bridge false: {tx_hash}')
            
    except Exception as error:
        fun.log_error(f"Ошибка: {error}")
        save_wallet_to("error_mint1", private_key)

    fun.timeOut("teh")  




    fun.timeOut() 
    
log("Ну типа все!")