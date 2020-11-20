# create a path and all the excel file should be in that path
# run the program into that path to get the required result

import openpyxl,csv,os

def execl_To_csv(path):

    for excelfile in os.listdir(path):

        if not excelfile.endswith('.xlsx'):
            continue
        wb = openpyxl.load_workbook(excelfile)

        for sheets in wb.get_sheet_names(): 

            sheet = wb.get_sheet_by_name(sheets)
            #sheet = wb.active 

            csvfile_name = excelfile.split('.')[0] + '_'+sheet.title+'.csv'

            csvfile_obj = open(csvfile_name,'w',newline='')

            csvfile_write = csv.writer(csvfile_obj)

            for row in sheet.rows:

                data = []

                for cell in row:

                    data.append(cell.value)

                csvfile_write.writerow(data)

            csvfile_obj.close()

        




if __name__ == '__main__':

    execl_To_csv("E:/Useful programme/excel")
