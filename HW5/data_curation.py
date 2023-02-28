from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


def data_curation(from_year, to_year, file_name):
    # https://www.geeksforgeeks.org/how-to-use-xpath-with-beautifulsoup/
    driver = webdriver.Chrome()
    driver.get("https://www.aos.wisc.edu/~sco/lakes/Mendota-ice.html")
    with open(file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["year", "days"])
        num_centers = len(driver.find_elements(By.XPATH, "/html/body/center"))
        year_array = []
        days_array = []

        for i in range(1, num_centers + 1):
            num_td = len(driver.find_elements(By.XPATH, f"/html/body/center[{i}]/table/tbody/tr["
                                                        f"2]/td"))
            for j in range(4, num_td + 1, 5):
                print(f"i: {i}, j: {j}")
                year_index = j - 3
                days_index = j
                # print(f"year_index: {year_index}, days_index: {days_index}")
                try:
                    year_col = driver.find_element(By.XPATH,
                                                   f"/html/body/center[{i}]/table/tbody/tr["
                                                   f"2]/td[{year_index}]/p/font")
                except:
                    year_col = driver.find_element(By.XPATH,
                                                   f"/html/body/center[{i}]/table/tbody/tr["
                                                   f"2]/td[{year_index}]/font")
                try:
                    days_col = driver.find_element(By.XPATH,
                                                   f"/html/body/center[{i}]/table/tbody/tr["
                                                   f"2]/td[{days_index}]/p/font")
                    if i == 4 and j == 9:
                        raise Exception("go to except")
                except:
                    days_col = driver.find_element(By.XPATH,
                                                   f"/html/body/center[{i}]/table/tbody/tr["
                                                   f"2]/td[{days_index}]/font")
                    # /html/body/center[4]/table/tbody/tr[2]/td[9]/font

                # append to array
                year_array += year_col.text.splitlines()
                days_array += days_col.text.splitlines()

        for k in range(0, len(days_array)):
            if year_array[k] == "\"":
                continue

            if k + 1 < len(days_array) and year_array[k + 1] == "\"":
                days = days_array[k + 1].strip()
                year = year_array[k].split("-")[0]
            elif days_array[k] == "---":  # no data
                days = 0
                year = year_array[k].split("-")[0]
            else:  # normal case
                days = days_array[k].strip()
                year = year_array[k].split("-")[0]

            print(f"year: {year}, days: {days}")
            if from_year <= int(year) <= to_year:
                writer.writerow([year, days])
    driver.close()


data_curation(1855, 2021, "hw5.csv")
