import win32com.client as win32
import os

root_script = os.getcwd()

wb_path = os.path.join(root_script, 'add_a_workbook.xls')
if os.path.exists(wb_path):
    os.remove(wb_path)

excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Add()
ws = wb.Worksheets.Add()
ws.Name = "Table"

# write table headers
ws.Cells(1, 1).Value = "InstallPath"
ws.Cells(1, 2).Value = "Name"
ws.Cells(1, 3).Value = "Path"
ws.Cells(1, 4).Value = "SnapName"
ws.Cells(1, 5).Value = "Done"



ws.Cells(2, 1).Value = r"\\rum\dfs\new_versions\CFW-2020\CFW-2020PR-4691_x64__git--efd_dev.4691_02.08.2019_1"
ws.Cells(3, 1).Value = r"\\rum\dfs\new_versions\CFW-2020\CFW-2020PR-4691_x64__git--efd_dev.4691_02.08.2019_1"

ws.Cells(2, 2).Value = "Windows 7 x64"
ws.Cells(3, 2).Value = "Windows 7 x64 Chi"

ws.Cells(2, 3).Value = r"D:\Images\Windows 7 x64\Windows 7 x64.vmx"
ws.Cells(3, 3).Value = r"D:\Images\Windows 7 x64 Chi\Windows 7 x64 Chi.vmx"

ws.Cells(2, 4).Value = "Creo 3.0"
ws.Cells(3, 4).Value = "Creo 3.0"

ws.Cells(2, 5).Value = "0"
ws.Cells(3, 5).Value = "0"



wb.SaveAs(wb_path, 56)
excel.Application.Quit()
