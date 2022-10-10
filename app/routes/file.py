from datetime import date, datetime
from fastapi import APIRouter, Depends
import xlrd
import pandas as pd
from app.services.file import (outputImage)
router = APIRouter(prefix="/file")
@router.get("/")
async def readfile():
    sheets = pd.ExcelFile('sample.xlsx').sheet_names
    excelPath = r'sample.xlsx'
    xls = pd.ExcelFile(excelPath)
    # df = pd.read_excel("sample.xlsx",na_filter = False)
    # print("Columns")
    # print(type(df))
    # print(df.columns)
    sheetDataDict = dict()
    print('start to read sheet...')
    for i in sheets:
        print('read sheeet from excel, sheet name:',i,'...')
        fh_tmp = pd.read_excel(excelPath,sheet_name = i)
        sheetDataDict[i] = fh_tmp
    # print(list(sheetDataDict.values())[1])
    col = pd.DataFrame(list(sheetDataDict.values())[1])
    data = col[['耗材名稱','上料時間','下料時間']]
    print("-----------------------------------------------------------")
    #我們也可以將每一行作為一個單獨的字典傳遞給函式 records。最後的結果是一個列表，
    #每一行都是一個字典。例如：
    sumDataDict = dict()
    fixDateDict = dict()

    useDataDict = data.to_dict('records')
    for i in useDataDict:
        if sumDataDict.__contains__(i['耗材名稱']):
            diff = datetime.date(i['下料時間']) - datetime.date(i['上料時間'])
            number = sumDataDict[i["耗材名稱"]]
            fixDateDict[i["耗材名稱"]].append(diff.days)
            sumDataDict[i["耗材名稱"]] = number +1
        else:
            # print(i["耗材名稱"])
            diff = datetime.date(i['下料時間']) - datetime.date(i['上料時間'])
            fixDateDict.setdefault(i["耗材名稱"],[diff.days])
            sumDataDict.setdefault(i["耗材名稱"],1)
    test = pd.DataFrame(list(sumDataDict.items()),columns=['耗材名稱','使用數量'])
    print(fixDateDict)
    print(test)
        
    return useDataDict