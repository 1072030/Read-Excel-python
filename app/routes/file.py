from fastapi import APIRouter, Depends
import xlrd
import pandas as pd
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
        
    print('end to read sheet!') 
    print(sheetDataDict.keys())
    print("內容物")
    col = list(sheetDataDict.values())[1].keys()
    print(col)
    
    return 