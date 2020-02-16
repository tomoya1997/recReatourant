import csv
import os
import operator

class Csv():
    def __init__(self):
        self.exist = os.path.isfile('package/csv_file/restaurant.txt')
        if not self.exist:
            with open('package/csv_file/restaurant.txt', 'w') as csv_file:
                fieldnames = ['Name', 'Count']
                writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                writer.writeheader()
        else:
            self.read()

    def write(self, restaurant):
        print(restaurant)
        print(self.restaurants)
        if restaurant in self.restaurants:
            with open('package/csv_file/restaurant.txt', 'w') as csv_file:
                fieldnames = ['Name', 'Count']
                writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                writer.writeheader()
            for k,v in self.restaurants.items():
                if k == restaurant:
                    v += 1
                with open('package/csv_file/restaurant.txt', 'a') as csv_file:
                    fieldnames = ['Name', 'Count']
                    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                    count = 1
                    writer.writerow({'Name': k, 'Count': v})
        else:
            with open('package/csv_file/restaurant.txt', 'a') as csv_file:
                fieldnames = ['Name', 'Count']
                writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                count = 1
                writer.writerow({'Name': restaurant, 'Count': count})
    
    def read(self):
        with open('package/csv_file/restaurant.txt', 'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            self.restaurants = {}
            for row in reader:
                # self.restaurants = {"Name": row['Name'], "Count": row['Count']}
                self.restaurants[row['Name']] = int(row['Count'])

    def populerRestaurants(self):
        restaurants = sorted(self.restaurants.items())
        return restaurants