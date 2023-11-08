import json
import os
from datetime import datetime
import random
from statistics import mean
import time
import requests
from web3 import Web3
import config


# option bsc / avax / fantom / polygon / arbitrum / optimism
address = {
    'polygon': {
        'type': 2,
        'chainId': 137,
        'rpc': config.rpc_links['polygon'],
        'USDC': '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174',
        'USDT': '0xc2132D05D31c914a87C6611C10748AEb04B58e8F',
        'MATIC': 'native',
        'native': 'MATIC',
        'WMATIC': '0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270',
        'lzChainId': 109,
        'merkly_gas_refuel': '0xa184998ec58dc1da77a1f9f1e361541257a50cf4',        

    },
    'arbitrum': {
        'type': 2,
        'rpc': config.rpc_links['arbitrum'],
        'USDC': '0xff970a61a04b1ca14834a43f5de4533ebddb5cc8',
        'USDT': '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9',
        'ETH': 'native',
        'native': 'ETH',
        'WETH': '0x82af49447d8a07e3bd95bd0d56f35241523fbab1',
        'lzChainId': 110,
        'merkly_gas_refuel': '0xaa58e77238f0e4a565343a89a79b4addd744d649',

    },
    'optimism': {
        'type': 2,
        'rpc': config.rpc_links['optimism'],
        'USDC': '0x7f5c764cbc14f9669b88837ca1490cca17c31607',
        'ETH': 'native',
        'native': 'ETH',
        'WETH': '0x4200000000000000000000000000000000000006',
        'lzChainId': 111,
        'merkly_gas_refuel': '0xa2c203d7ef78ed80810da8404090f926d67cd892',

    },
    'bsc': {
        'type': 0,
        'chainId': 56,
        'rpc': config.rpc_links['bsc'],
        'USDT': '0x55d398326f99059ff775485246999027b3197955',
        'BUSD': '0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56',
        'BNB': 'native',
        'native': 'BNB',
        'WBNB': '0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c',
        'lzChainId': 102,
        'merkly_gas_refuel': '0xfdc9018af0e37abf89233554c937eb5068127080',

    },
    'fantom': {
        'type': 2,
        'rpc': config.rpc_links['fantom'],
        'USDC': '0x04068DA6C83AFCFA0e13ba15A6696662335D5B75',
        'FTM': 'native',
        'native': 'FTM',
        'WFTM': '0x21be370D5312f44cB42ce377BC9b8a0cEF1A4C83',
        'lzChainId': 112,
        'merkly_gas_refuel': '0x97337a9710beb17b8d77ca9175defba5e9afe62e',

    },
    'avax': {
        'type': 2,        
        'rpc': config.rpc_links['avax'],
        'USDC': '0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E',
        'USDT': '0x9702230a8ea53601f5cd2dc00fdbc13d4df4a8c7',
        'AVAX': 'native',
        'native': 'AVAX',
        'WAVAX': '0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7',
        'lzChainId': 106,
        'merkly_gas_refuel': '0xe030543b943bdcd6559711ec8d344389c66e1d56',

    },
    'aptos': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 108,
        'merkly_gas_refuel': '',

    },
    'dfk': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 115,
        'merkly_gas_refuel': '',

    },
    'harmony': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 116,
        'merkly_gas_refuel': '0x885ef5813E46ab6EFb10567b50b77aAAD4d258ce',

    },
    'dexalot': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 118,
        'merkly_gas_refuel': '',

    },
    'celo': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 125,
        'merkly_gas_refuel': '0xE33519C400B8F040E73aeDa2f45DfDD4634A7cA0',

    },
    'moonbeam': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 126,
        'merkly_gas_refuel': '0x766b7aC73b0B33fc282BdE1929db023da1fe6458',

    },
    'fuse': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 138,
        'merkly_gas_refuel': '0xFFd57B46BD670B0461c7C3EBBaEDC4CdB7c4FB80',

    },
    'gnosis': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 145,
        'merkly_gas_refuel': '0xb58f5110855fbef7a715d325d60543e7d4c18143',

    },
    'klaytn': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 150,
        'merkly_gas_refuel': '0xd02ffae68d902453b44a9e45dc257aca54fb88b2',

    },
    'metis': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 151,
        'merkly_gas_refuel': '0x2E228120c0AF2dE3A74D744B25B24D1fb28CE5B4',

    },
    'coredao': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 153,
        'merkly_gas_refuel': '0xCA230856343C300f0cc2Bd77C89F0fCBeDc45B0f',

    },
    'okt': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 155,
        'merkly_gas_refuel': '0xa0a54dADc2a1F198C58Fd0739BA7dF40Ffd366Dc',

    },
    'zkevm': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 158,
        'merkly_gas_refuel': '0xb58f5110855fBEF7A715d325D60543E7D4c18143',

    },
    'canto': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 159,
        'merkly_gas_refuel': '0x426A8Dc7263A439e92972eE2200DA21EC6cEEcfa',

    },
    'zksyncera': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 165,
        'merkly_gas_refuel': '0x6dd28C2c5B91DD63b4d4E78EcAC7139878371768',

    },
    'moonriver': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 167,
        'merkly_gas_refuel': '0x97337A9710BEB17b8D77cA9175dEFBA5e9AFE62e',

    },
    'tenet': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 173,
        'merkly_gas_refuel': '0x83d8476eBccf8094d80D7b2165375a3Ec4E93034',

    },
    'nova': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 175,
        'merkly_gas_refuel': '0x484c402B0c8254BD555B68827239BAcE7F491023',

    },
    'meter': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 176,
        'merkly_gas_refuel': '0xd81a2e87232b4fdd27fbe16107d8deaaa2d14181',

    },
    'sepolia': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 161,
        'merkly_gas_refuel': '0xf836905A5C6E9dFBB88c4a9ADf79f6a47B43eCBB',

    },
    'kava': {
        'type': 0,        
        'rpc': '',
        'lzChainId': 177,
        'merkly_gas_refuel': '0x04866796aabB6B58e6bC4d91A2aE99105b2C58AE',

    },
    'scroll': {
        'type': 0,        
        'rpc': 'https://rpc.ankr.com/scroll',
        'ETH': 'native',
        'native': 'ETH',        
        'lzChainId': 214,
        'merkly_gas_refuel': '',

    }


}


log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_file = f"{log_dir}/{datetime.now().strftime('%Y-%m-%d_%H-%M')}.log"

erc20_abi = json.load(open('abi/erc20_abi.json'))
bridge_abi = json.load(open('abi/brige_abi.json'))



def get_token_balance(wallet, network, token ):
    try:
        web3 = Web3(Web3.HTTPProvider(address[network]['rpc'], request_kwargs=config.request_kwargs))
        wallet = Web3.to_checksum_address(wallet)

        if address[network][token]=="native":
            balance = web3.eth.get_balance(wallet)
            balance = Web3.from_wei(balance, 'ether')
        else:
            erc20_address = web3.to_checksum_address(address[network][token])
            erc20_contract = web3.eth.contract(address=erc20_address, abi=erc20_abi)
            token_decimals = erc20_contract.functions.decimals().call()
            balance = erc20_contract.functions.balanceOf(wallet).call() / 10 ** token_decimals
        time.sleep(2)    
            
        return balance

    except Exception as error:
        return log_error(f'{network} {token} | Ошибка при получении баланса токенов: Проблема либо в rpc, либо в связке rpc-proxy, либо проблемы с самой сетью.')


def get_token_balance_USD(wallet, network, token ):
    try:
        result = get_token_balance(wallet, network, token )
        if result == "error":
            return "error"
        balance = float(result)
        return balance*config.prices[token]

    except Exception as error:
        return log_error(f'{network} {token} | Ошибка при переводе баланса токенов в USD: {error}')


def log(text, status=""):
    now = datetime.now()
    log_text = now.strftime('%d %H:%M:%S')+": "
    with open(log_file, "a", encoding='utf-8') as f:
        if status == "error":
            color_code = "\033[91m"  # red
            log_text = log_text + "ERROR: "
        elif status == "ok":
            color_code = "\033[92m"  # green
            log_text = log_text + "OK: "
        else:
            color_code = "\033[0m"  # white
        log_text = log_text + f"{text}"
        log_text_color = f"{color_code}{log_text}\033[0m"
        f.write(log_text + "\n")
        print(log_text_color)

def log_error(text):
    log(text, "error")
    return "error"

def log_error_critical(text):
    log(text, "error")
    f=open(f"{log_dir}/critical.log", "a", encoding='utf-8')
    f.write(text + "\n")    
    return "error"

def log_ok(text):
    log(text, "ok")
    return "ok"

def save_wallet_to(filename, wallet):
    f=open(f"{log_dir}/{filename}.log", "a", encoding='utf-8')
    f.write(wallet + "\n")    


def timeOut(type="main"):
    if type=="main":
        time_sleep=random.randint(config.timeoutMin, config.timeoutMax)
    if type=="teh":
        time_sleep=random.randint(config.timeoutTehMin, config.timeoutTehMax)
        
    if int(time_sleep/60) > 0:
        log(f"пауза {int(time_sleep/60)} минут")
    time.sleep(time_sleep)

def get_new_prices(token = False):


    if token:
        try:
            url =f'https://min-api.cryptocompare.com/data/price?fsym={token}&tsyms=USDT'
            result = requests.get(url=url, proxies=config.proxies)
            if result.status == 200:
                resp_json = result.json(content_type=None)
                new_price = float(resp_json['USDT'])
                config.prices[token] = new_price
                log(f"Обновил цену для {token}= {new_price}")
        except Exception as error:
            log_error(f'Не смог узнать цену для {token}: {error}')

    else:
            
        if config.prices["last_update"] > int(time.time()-3600):
            return False
        config.prices["last_update"] = int(time.time())

        for token, price in config.prices.items():    
            if token == "last_update":
                continue

            try:
                url =f'https://min-api.cryptocompare.com/data/price?fsym={token}&tsyms=USDT'
                if config.proxy_use:
                    result = requests.get(url=url, proxies=config.proxies)
                else:
                    result = requests.get(url=url)                    
                if result.status_code == 200:
                    resp_json = result.json()
                    new_price = float(resp_json['USDT'])
                    config.prices[token] = new_price
                    log(f"Обновил цену для {token}= {new_price}")
            except Exception as error:
                log_error(f'Не смог узнать цену для {token}: {error}')

            time.sleep(1)

    return True