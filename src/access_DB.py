from SPARQLWrapper import SPARQLWrapper
import csv
import util_DBpedia
import util

def get_value_DBpedia(querys):
    results = []
    sparql = SPARQLWrapper(
        endpoint='http://ja.dbpedia.org/sparql',returnFormat='json')
    for query in querys:
        sparql.setQuery("""                                                                                                                                                                      
            PREFIX dbpj: <http://ja.dbpedia.org/resource/%s>
            PREFIX dbo:  <http://dbpedia.org/ontology/>
            
            SELECT DISTINCT ?property ?description where {
                {
                    dbpj: ?property ?description .FILTER( !contains(str(?description), 'http://' ) && !contains(str(?property),'wikiPage') && !contains(str(?property), 'http://www.w3.org/2000/01/rdf-schema'))
                }
                UNION
                {
                    ?link ?property dbpj: .FILTER( contains(str(?link), 'http://ja.dbpedia.org/resource/' ) && !contains(str(?link),'Category'))
                    ?link dbo:abstract ?description
                }
                UNION
                {
                    dbpj: ?property ?link .FILTER( contains(str(?link), 'http://ja.dbpedia.org/resource/' ) && !contains(str(?link),'Category')&& !contains(str(?property),'Template'))
                    ?link dbo:abstract ?description
                }
                UNION
                {
                    dbpj: ?property ?link  .FILTER( contains(str(?link),'Category')).
                    ?link <http://www.w3.org/2000/01/rdf-schema#label> ?description
                }
            } 
            """%(query))
        result = sparql.query()
        result = result.convert()
        results.append({query: result})
    return results

def get_data_csv(file_path):
    with open(file_path) as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    return data

if __name__ == "__main__":
    save_path = "./result_data/result.csv"
    # keywords は,"data/jaqket_train.json"の質問に対する固有抽出結果
    keywords_path = "./result_data/keywords.csv"
    keywords_list = get_data_csv(keywords_path)
    results_list = get_value_DBpedia(keywords_list[0])
    outputs = []
    for reuslt in results_list:
        key = list(reuslt.keys())
        row_values = [util_DBpedia.get_start(value) for value in reuslt.values()][0]
        value = util_DBpedia.get_value(row_values)
        for val in value:
            outputs.append(key + val)
    util.write_value(save_path, outputs)