import os, sys

path_to_project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path_to_project)
os.environ["DJANGO_SETTINGS_MODULE"] = "project.settings.dev"
import django
import csv

django.setup()

from provider.models import ProviderAvailibility

if __name__ == "__main__":

    PROVIDER_CODE_NAME = (
        ("20801", "Orange"),
        ("20810", "SFR"),
        ("20815", "FREE"),
        ("20820", "Bouygues"),
    )

    with open(
        "data/2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93_template.csv"
    ) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        list_of_provider = []
        count_line = 0

        # We create a list from csv
        for row in csv_reader:
            if count_line == 0:
                print(f'Headers of csv are {", ".join(row)}')
                count_line += 1
            else:
                ProviderAvailibility.objects.create(
                    provider_code=row[0],
                    lamb_x_coord=row[1],
                    lamb_y_coord=row[2],
                    availibility_2G=row[3],
                    availibility_3G=row[4],
                    availibility_4G=row[5],
                )

                if count_line % 200 == 0:
                    print("Inserted:" + str(count_line))
                count_line += 1
        print(f"Processed {count_line} lines.")
