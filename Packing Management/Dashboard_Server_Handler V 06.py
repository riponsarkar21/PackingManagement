# version 06: 
# 2024.10.05 : use shortcut file as Source file  


import xlwings as xw
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to copy data from the source file to the target file
def copy_data_to_dashboard(source_file, target_sheet, start_row, copy_titles=False):
    """
    Copies production and bursting data from the source Excel file into the target Excel sheet.
    
    :param source_file: Path to the source Excel file
    :param target_sheet: The target Excel sheet object to copy data into
    :param start_row: Row number in the target sheet where data should start being copied
    :param copy_titles: If True, copies the title row (headers); if False, skips the title row
    :return: The next available row in the target sheet after copying data
    """
    logging.info(f"Processing file: {source_file}")
    
    # Open the source workbook
    try:
        wb = xw.Book(source_file)
        sheet = wb.sheets["Production Details by Shift (2)"]

        # Unprotect the sheet if it's protected
        if sheet.api.ProtectContents:
            logging.info("Unprotecting sheet...")
            sheet.api.Unprotect(Password="Ripon")

        # Read data ranges from the source sheet
        logging.info("Reading data from the source sheet.")
        source_range_Date = sheet.range("A5:A35").value

        # Read title row (FI4:FV4) for production data
        source_production_range_brand_title = sheet.range("FI4:FV4").value
        source_bursting_range_brand_title = sheet.range("IW4:JJ4").value

        # Read production and bursting data
        source_production_ranges = {
            '1A': sheet.range("FI5:FV35").value,
            '1B': sheet.range("FX5:GK35").value,
            '1C': sheet.range("GM5:GZ35").value,
            '2A': sheet.range("HC5:HP35").value,
            '2B': sheet.range("HR5:IE35").value,
            '2C': sheet.range("IG5:IT35").value,
        }

        source_bursting_ranges = {
            '1A': sheet.range("IW5:JJ35").value,
            '1B': sheet.range("JL5:JY35").value,
            '1C': sheet.range("KA5:KN35").value,
            '2A': sheet.range("KQ5:LD35").value,
            '2B': sheet.range("LF5:LS35").value,
            '2C': sheet.range("LU5:MH35").value,
        }

        # Transpose source dates for vertical pasting
        source_range_Date = [[item] for item in source_range_Date]

        # Initialize current_row to the passed start_row
        current_row = start_row

        # Write the dates to the target sheet
        logging.info("Writing date and shift data to the target sheet.")
        for i in range(6):
            target_sheet.range(f"D{current_row + 31 * i}:D{current_row + 30 + 31 * i}").value = source_range_Date
            shift_letter = "ABC"[i % 3]  # Alternates A, B, C
            shift_number = 1 if i < 3 else 2
            target_sheet.range(f"E{current_row + 31 * i}:E{current_row + 30 + 31 * i}").value = shift_letter
            target_sheet.range(f"F{current_row + 31 * i}:F{current_row + 30 + 31 * i}").value = shift_number

        # Write title row if this is the first file
        if copy_titles:
            logging.info("Copying title rows.")
            target_sheet.range(f"G1").value = source_production_range_brand_title
            target_sheet.range(f"BE1").value = source_bursting_range_brand_title

        # Write production data
        logging.info("Writing production data.")
        target_sheet.range(f"G{current_row}").value = source_production_ranges['1A']
        target_sheet.range(f"G{current_row + 31}").value = source_production_ranges['1B']
        target_sheet.range(f"G{current_row + 62}").value = source_production_ranges['1C']
        target_sheet.range(f"G{current_row + 93}").value = source_production_ranges['2A']
        target_sheet.range(f"G{current_row + 124}").value = source_production_ranges['2B']
        target_sheet.range(f"G{current_row + 155}").value = source_production_ranges['2C']

        # Write bursting data
        logging.info("Writing bursting data.")
        target_sheet.range(f"BE{current_row}").value = source_bursting_ranges['1A']
        target_sheet.range(f"BE{current_row + 31}").value = source_bursting_ranges['1B']
        target_sheet.range(f"BE{current_row + 62}").value = source_bursting_ranges['1C']
        target_sheet.range(f"BE{current_row + 93}").value = source_bursting_ranges['2A']
        target_sheet.range(f"BE{current_row + 124}").value = source_bursting_ranges['2B']
        target_sheet.range(f"BE{current_row + 155}").value = source_bursting_ranges['2C']

        # Close the source workbook
        wb.close()

        # Return the next available row after data has been written
        logging.info(f"Data from {source_file} copied successfully.")
        return current_row + 187  # Total rows copied is 187

    except Exception as e:
        logging.error(f"Error processing file {source_file}: {e}")
        if 'wb' in locals():
            wb.close()  # Ensure workbook is closed in case of error
        return start_row  # In case of error, return the same start_row


# File paths and configuration
source_folder = r"ProductionFile\2024"
# target_file = r"F:\Packing\Packing All Backup\Ripon\Important Packing Ripon\E_Dashboard\Server\Dashboard - V06.xlsx"
target_file = r"Server\production_report_server.lnk"

# Get list of source files
source_files = [
    "Jan 24 Shun Shing Cement Industries Ltd - Shortcut.lnk",
    "Feb 24 Shun Shing Cement Industries Ltd - Shortcut.lnk",
    "Mar 24 Shun Shing Cement Industries Ltd - Shortcut.lnk",
    "Apr 24 Shun Shing Cement Industries Ltd - Shortcut.lnk",
    "May 24 Shun Shing Cement Industries Ltd - Shortcut.lnk",
    "Jun 24 Shun Shing Cement Industries Ltd - Shortcut.lnk",
    "Jul 24 Shun Shing Cement Industries Ltd - Shortcut.lnk",
    "Aug 24 Shun Shing Cement Industries Ltd - Shortcut.lnk",
    "Sep 24 Shun Shing Cement Industries Ltd - Shortcut.lnk",
    "Oct 24 Shun Shing Cement Industries Ltd - Shortcut.lnk",
    "Nov 24 Shun Shing Cement Industries Ltd - Shortcut.lnk"
    
]

# Open the target workbook and the relevant sheet
target_wb = xw.Book(target_file)
target_sheet = target_wb.sheets["Imported Production Data Bag"]

# Start copying data from row 2 onwards
start_row = 2

# Loop through source files and copy data
for idx, file_name in enumerate(source_files):
    source_file = os.path.join(source_folder, file_name)
    
    # Copy titles only for the first file
    copy_titles = (idx == 0)
    
    # Copy data from the source file to the target file
    start_row = copy_data_to_dashboard(source_file, target_sheet, start_row, copy_titles)

# Save the target workbook after all data is copied
target_wb.save()

# Close the target workbook
target_wb.close()

logging.info("Data copied successfully from all source files to the dashboard.")
print("Data copied successfully from all source files to the dashboard.")

