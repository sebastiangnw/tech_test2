"""Graphics views"""

import os
from google.cloud import bigquery

# Create your views here.


def bigqueryview(request):
    """Bigquery view"""
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "pruebatech-404819-c4fc8d25c7e3.json"

    client = bigquery.Client()

    sql_query = """
    SELECT country_name, region_name, term, rank, refresh_date
    FROM `bigquery-public-data.google_trends.international_top_terms` 
    WHERE refresh_date = "2023-10-26" 
    LIMIT 10
    """

    query_job = client.query(sql_query)

    for row in query_job.result():
        print(row)
