import wx
import wx.grid
import thread
import time
import random
from ib.ext.Contract import Contract
from ib.opt import ibConnection, message


def makeStkContract(contractTuple):
    newContract = Contract()
    newContract.m_symbol = contractTuple[0]
    newContract.m_secType = contractTuple[1]
    newContract.m_exchange = contractTuple[2]
    newContract.m_currency = contractTuple[3]
    return newContract



def my_contract_handler(msg):
    print msg
    for property, value in vars(msg.contractDetails).iteritems():
        print property, ": ", value
    for property, value in vars(msg.contractDetails.m_summary).iteritems():
        print property, ": ", value




if __name__ == '__main__':
    con = ibConnection()
    contractTuple = [('AUD', 'CASH', 'IDEALPRO', 'USD')]
    #con.register(my_contract_handler, message.ContractDetails, message.ContractDetailsEnd)
    con.register(my_contract_handler, message.ContractDetails)
    con.connect()
    stkContract = makeStkContract(contractTuple[0])

    con.reqContractDetails(1,stkContract)
    time.sleep(1)