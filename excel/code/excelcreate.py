def create_workbook(code,value,savepath):

    from openpyxl.workbook import Workbook
    import os

    headers = ['提示','序号','机构标识','股东简称','股东全称','性别','证件类别','证件号码','证件地址','法定代表人姓名','法定代表人证件类别','经办人姓名','法定代表人证件编号','经办人证件类别','经办人证件编号','联系地址','联系方式','股权性质','股权数量（股）','实缴数量','股东性质','确权标识','控制股份数','开户银行','银行账号','实际入股金额','投票权数','持有其他股权所在银行名称','持有家数','在本企业派驻董监高人员情况','股权证书状态','外部账号','是否为内部职工','出资日期','是否为发起人股东','是否为控股股东','是否为主要股东','是否为董监高成员','备注']

    workbook_name = code+'.xlsx'
    
    wb = Workbook()
    page = wb.active
    page.title = 'sheet1'
    page.append(headers)
    for item in value:
        page.append(item)
    wb.save(os.path.join(savepath,workbook_name))
    print('文件名:',os.path.join(savepath,workbook_name),'创建成功\n###################')
