import os
from datetime import datetime
from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# ===================================================  Dashboard ==================================================

# # New route to open Version file
# @app.route('/version')
# def version():
#     # file_path = r"static\files\version.txt"
#     # os.startfile(file_path)  # This will open the file using the default associated application (Excel)
#     return redirect(url_for('version'))  # Redirect back to the All Reports page after opening the file



@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/production_management')
def production_management():
    return render_template('production_management.html')

@app.route('/maintenance_management')
def maintenance_management():
    return render_template('maintenance_management.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/maintenance_management')
def maintenance_management3():
    return render_template('maintenance_management.html')

@app.route('/manpower')
def manpower():
    return render_template('manpower.html')

@app.route('/kpi')
def kpi():
    return render_template('kpi.html')

@app.route('/maintenance_management')
def maintenance_management6():
    return render_template('maintenance_management.html')

@app.route('/maintenance_management')
def maintenance_management7():
    return render_template('maintenance_management.html')


# ===================================================  All Reports ==================================================

def get_file_path(month_year):
    file_mapping = {
        'Jan-2024': r'static\files\2024\Jan 24 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Feb-2024': r'static\files\2024\Feb 24 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Mar-2024': r'static\files\2024\Mar 24 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Apr-2024': r'static\files\2024\Apr 24 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'May-2024': r'static\files\2024\May 24 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Jun-2024': r'static\files\2024\Jun 24 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Jul-2024': r'static\files\2024\Jul 24 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Aug-2024': r'static\files\2024\Aug 24 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Sep-2024': r'static\files\2024\Sep 24 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Oct-2024': r'static\files\2024\Oct 24 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Nov-2024': r'static\files\2024\Nov 24 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Dec-2024': r'static\files\2024\Dec 24 Shun Shing Cement Industries Ltd - Shortcut.lnk',

        'Jan-2023': r'static\files\2023\Jan 23 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Feb-2023': r'static\files\2023\Feb 23 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Mar-2023': r'static\files\2023\Mar 23 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Apr-2023': r'static\files\2023\Apr 23 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'May-2023': r'static\files\2023\May 23 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Jun-2023': r'static\files\2023\Jun 23 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Jul-2023': r'static\files\2023\Jul 23 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Aug-2023': r'static\files\2023\Aug 23 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Sep-2023': r'static\files\2023\Sep 23 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Oct-2023': r'static\files\2023\Oct 23 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Nov-2023': r'static\files\2023\Nov 23 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Dec-2023': r'static\files\2023\Dec 23 Shun Shing Cement Industries Ltd - Shortcut.lnk',

        'Jan-2022': r'static\files\2022\Jan 22 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Feb-2022': r'static\files\2022\Feb 22 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Mar-2022': r'static\files\2022\Mar 22 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Apr-2022': r'static\files\2022\Apr 22 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'May-2022': r'static\files\2022\May 22 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Jun-2022': r'static\files\2022\Jun 22 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Jul-2022': r'static\files\2022\Jul 22 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Aug-2022': r'static\files\2022\Aug 22 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Sep-2022': r'static\files\2022\Sep 22 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Oct-2022': r'static\files\2022\Oct 22 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Nov-2022': r'static\files\2022\Nov 22 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Dec-2022': r'static\files\2022\Dec 22 Shun Shing Cement Industries Ltd - Shortcut.lnk',

        'Jun-2021': r'static\files\2021\Jun 21 Shun Shing Cement Industres Ltd - Shortcut.lnk',
        'Jul-2021': r'static\files\2021\Jul 21 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Aug-2021': r'static\files\2021\Aug 21 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Sep-2021': r'static\files\2021\Sep 21 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Oct-2021': r'static\files\2021\Oct 21 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Nov-2021': r'static\files\2021\Nov 21 Shun Shing Cement Industries Ltd - Shortcut.lnk',
        'Dec-2021': r'static\files\2021\Dec 21 Shun Shing Cement Industries Ltd - Shortcut.lnk',


    }
    return file_mapping.get(month_year, None)
# -----------------------------------------------
# # this part ok 

# @app.route('/all_reports')
# def all_reports():
#     current_year = datetime.now().year
#     months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#     month_year_list = [f"{month}-{current_year}" for month in months]
#     return render_template('all_reports.html', month_year_list=month_year_list)
# =================================================

@app.route('/all_reports')
def all_reports():
    # current_year = datetime.now().year
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    years = ['2024','2023','2022','2021']
    month_list = [f"{month}" for month in months]
    year_list = [f"{year}" for year in years]
    return render_template('all_reports.html', month_list=month_list, year_list=year_list)



# @app.route('/open_report', methods=['POST'])
# def open_report():
#     month_year = request.form['monthYear']
#     file_path = get_file_path(month_year)

#     if file_path and os.path.exists(file_path):
#         os.startfile(file_path)  # This will open the file using the default associated application
#         return redirect(url_for('all_reports'))
#     else:
#         return f"File for {month_year} not found.", 404  # Handle case where file is not found





# =================== ok. but slow ======================

import win32com.client as win32
from flask import Flask, request, jsonify
import openpyxl

@app.route("/preview_report", methods=["POST"])
def preview_report():
    data = request.get_json()
    month = data.get("month")
    year = data.get("year")
    
    # Path to the .xlsm file
    file_path = r"F:\Packing\Packing All Backup\Ripon\Production Report\Production Report 2024 XL\Oct 24 Shun Shing Cement Industries Ltd.xlsm"
    
    try:
        # Load only the specific sheet you need, without recalculating formulas
        wb = openpyxl.load_workbook(file_path, data_only=True, keep_links=False)

        # Access the "Monthly" sheet directly
        sheet = wb["Monthly"]

        # Get the value from D32
        value = sheet["D32"].value

        # Close the workbook to release resources
        wb.close()

        # Send the value back to the frontend
        return jsonify({"value": value})
    except Exception as e:
        print(f"Error opening Excel file: {e}")
        return jsonify({"error": "Failed to open the Excel file"}), 500





@app.route('/open_report', methods=['POST'])
def open_report():
    # Get the selected month and year from the form
    selected_month = request.form['month']
    selected_year = request.form['year']
    
    # Combine month and year to create the necessary file name or path
    month_year = f"{selected_month}-{selected_year}"
    file_path = get_file_path(month_year)

    # Check if the file exists and open it
    if file_path and os.path.exists(file_path):
        os.startfile(file_path)  # This will open the file using the default associated application
        return redirect(url_for('all_reports'))
    else:
        return f"File for {selected_month} {selected_year} not found.", 404  # Handle case where file is not found




# New route to open Excel file
@app.route('/production_report_this_month')
def production_report_this_month():
    file_path = r"static\files\Production Report (This Month).lnk"
    os.startfile(file_path)  # This will open the file using the default associated application (Excel)
    return redirect(url_for('all_reports'))  # Redirect back to the All Reports page after opening the file


@app.route('/yearly_report')
def yearly_report():
    file_path = r"static\files\Yearly Summary & Run Time.lnk"
    os.startfile(file_path)
    return redirect(url_for('all_reports'))


@app.route('/bulk_bm')
def bulk_bm():
    file_path = r"static\files\Bulk Record BM.lnk"
    os.startfile(file_path)
    return redirect(url_for('all_reports'))

@app.route('/bulk_gold')
def bulk_gold():
    file_path = r"static\files\Bulk Record Gold.lnk"
    os.startfile(file_path)
    return redirect(url_for('all_reports'))

@app.route('/scbl_trawler')
def scbl_trawler():
    file_path = r"static\files\SCBL Trawler Details.lnk"
    os.startfile(file_path)
    return redirect(url_for('all_reports'))

@app.route('/fob_bulk_light_weight')
def fob_bulk_light_weight():
    file_path = r"static\files\FOB Bulk Light Weight.lnk"
    os.startfile(file_path)
    return redirect(url_for('all_reports'))



# ===================================================  KPI ==================================================

@app.route('/duty_register')
def duty_register():
    file_path = r"static\files\kpi\Duty Register for Packing.xlsx - Shortcut.lnk"
    os.startfile(file_path)
    return redirect(url_for('kpi'))

@app.route('/production_kpi')
def production_kpi():
    file_path = r"static\files\kpi\Packing Production Register.xlsx - Shortcut.lnk"
    os.startfile(file_path)
    return redirect(url_for('kpi'))

@app.route('/bursting_and_power')
def bursting_and_power():
    file_path = r"static\files\kpi\Packing Bursting and Power Consumption Record.xlsx - Shortcut.lnk"
    os.startfile(file_path)
    return redirect(url_for('kpi'))

@app.route('/weight_control')
def weight_control():
    file_path = r"static\files\kpi\Defective Equipment Register for Packing.xlsx - Shortcut.lnk"
    os.startfile(file_path)
    return redirect(url_for('kpi'))

@app.route('/short_excess')
def short_excess():
    file_path = r"static\files\kpi\Short Excess of Empty Bag Balance Record.xlsx - Shortcut.lnk"
    os.startfile(file_path)
    return redirect(url_for('kpi'))

@app.route('/defective_equipment')
def defective_equipment():
    file_path = r"static\files\kpi\Defective Equipment Register for Packing.xlsx - Shortcut.lnk"
    os.startfile(file_path)
    return redirect(url_for('kpi'))

# ===================================================  production report ==================================================

from flask import Flask, render_template, request, jsonify
import xlwings as xw
import os


# Function to update Excel with the selected values
def update_excel(from_date, to_date, shift, unit, brand):
    try:
        # Create an instance of Excel in hidden mode
        app_xl = xw.App(visible=False)  # Set Excel visibility to False
        app_xl.screen_updating = False  # Disable screen updating for better performance

        # Verify the Excel file exists
        excel_path = r'Server\production_report_server.lnk'
        if not os.path.exists(excel_path):
            raise FileNotFoundError(f"Excel file not found at: {excel_path}")

        # Open the workbook through the hidden Excel instance
        wb = app_xl.books.open(excel_path)
        sheet = wb.sheets['Sorted Bag']

        # Paste the selected values in the Excel sheet
        sheet.range('A5').value = from_date
        sheet.range('B5').value = to_date
        sheet.range('C5').value = shift
        sheet.range('D5').value = unit
        sheet.range('E5').value = brand

        # Get the production value from F5
        production_value = sheet.range('F5').value

        # Save and close the workbook
        wb.save()
        wb.close()

        # Quit the hidden Excel instance
        app_xl.quit()

        return production_value

    except Exception as e:
        # Log any errors encountered
        print(f"Error in update_excel: {e}")
        if 'app_xl' in locals():
            app_xl.quit()  # Ensure Excel quits even if an error occurs
        return None

@app.route('/production_report', methods=['GET', 'POST'])
def production_report():
    if request.method == 'POST':
        from_date = request.form['from_date']
        to_date = request.form['to_date']
        shift = request.form['shift']
        unit = request.form['unit']
        brand = request.form['brand']

        production_value = update_excel(from_date, to_date, shift, unit, brand)

        if production_value is None:
            return jsonify({"error": "Failed to retrieve production data"}), 500

        return jsonify({"production": production_value})
    
    return render_template('production_report.html')


# ===================================================  Closing ==================================================


if __name__ == '__main__':
    app.run(debug=True, port=5001)