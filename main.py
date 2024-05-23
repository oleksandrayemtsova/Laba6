import pandas as pd


class DataProcessor:
    def __init__(self, file_path, delimiter=',', header=True):
        try:
            self.data_frame = pd.read_csv(file_path, delimiter=delimiter, header=0 if header else None)
        except Exception as e:
            raise Exception("Unfortunately, we were unable to read the data file. Error: {}".format(str(e)))

    def list_of_all_countries(self):
        print("*"*100)
        print("List of all countries: ")
        return self.data_frame

    def population_over_10m(self):
        print("*"*100)
        print("Countries with population over 10 million:")
        return (self.data_frame[self.data_frame['Population'] > 10_000_000] [['Country', 'Population']])

    def population_area_larger_than_ukraine_and_more_than_10m(self, ukraine_area):
        print("*"*100)
        print("Countries with population over 10 million and area greater than Ukraine:")
        population = 10_000_000
        population_condition = self.data_frame['Population'] > population
        area_condition = self.data_frame['Area (sq. mi.)'] > ukraine_area
        return (self.data_frame[population_condition & area_condition][['Country', 'Population', 'Area (sq. mi.)']])

    def top_10_countries_in_agriculture(self):
        print("*"*100)
        print("Top 10 countries in agriculture:")
        return (self.data_frame.nlargest(10, 'Agriculture')[['Country', 'Agriculture']])

    def countries_bordering_the_sea(self):
        print("*"*100)
        print("Countries bordering sea:")
        return (self.data_frame[self.data_frame['Coastline (coast/area ratio)'] > 0] [['Country', 'Coastline (coast/area ratio)']])


if __name__ == '__main__':
    processor = DataProcessor('countries_of_the_world.csv')
    print(processor.list_of_all_countries())
    print(processor.population_over_10m())
    print(processor.population_area_larger_than_ukraine_and_more_than_10m(603_700))
    print(processor.top_10_countries_in_agriculture())
    print(processor.countries_bordering_the_sea())
