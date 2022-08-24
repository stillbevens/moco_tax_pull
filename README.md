browser_get.py and browser_cleaner.py are used to get the true owner/entity and address of land in Montgomery County, MD tax sales. The tax sale website will host upcoming sales data but only provide the parcel ID. The parcel ID is not too useful on its own but can be used to query the tax website to get the true owner and address.

To use:
-Download the tax sale data as an xslx.
-update 'excel_data' variable in brower_get.py to read the previously downloaded data
-update 'workbook' variable where the real property information will be written too
-update 'browser' for the correct browser webdriver that selenium will use to do the queries

- run the browser_get.py and let it go through the entire list.
open the output xlsx to have all of the actual property information

For any failed attempts (not very robust, quick script to check my failures and indicate why):
-copy and paste the output failed list into 'parcels' of browser_cleaner.py
-this will do a more generic query to see why the initial failed
