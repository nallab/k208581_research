from SPARQLWrapper import SPARQLWrapper
import csv
import util_DBpedia
import util


def access_DBpedia():
    sparql = SPARQLWrapper(
        endpoint='http://ja.dbpedia.org/sparql', returnFormat='json')
    sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX category-ja: <http://ja.dbpedia.org/resource/Category:>
        PREFIX dbo:  <http://dbpedia.org/ontology/>

        select distinct ?pref ?p where {
            ?pref rdf:type dbo:Place.
            ?pref dbo:wikiPageWikiLink category-ja:日本の都道府県.
            ?pref ?p ?o .
        }GROUP BY ?pref
        """)
    result = sparql.query()
    result = result.convert()
    return result


def get_value(list_datas):
    all_value = []
    for data in list_datas:
        pref_value = data['pref']['value'].split("/")[-1]
        prop_value = data['p']['value']
        #value = data['o']['value']
        all_value.append([pref_value, prop_value])
    return all_value

if __name__ == "__main__":
    file_path = "./result_data/prefectures_japan.csv"
    results = access_DBpedia()
    results_format = util_DBpedia.get_start(results)
    result_value = get_value(results_format)
    util.write_value(file_path, result_value)
