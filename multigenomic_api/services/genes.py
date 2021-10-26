from ..models.genes import Genes
from . import base


def get_all() -> [Genes]:
    return base.get_all(Genes)


def find_by_id(id_: str) -> Genes:
    return base.find_one_by_id(Genes, id_)


def get_closest_genes_to_central_position(left_end_pos: int, right_end_pos: int, central_pos: float,
                                          max_distance: int) -> [Genes]:
    genes = Genes.objects(__raw__={"$or": [
                                      {"$and": [
                                          {"leftEndPosition": {"$gte": left_end_pos}},
                                          {"rightEndPosition": {"$lte": right_end_pos}}
                                      ]},
                                      {"$and": [
                                          {"leftEndPosition": {"$lt": left_end_pos}},
                                          {"rightEndPosition": {"$gt": left_end_pos, "$lte": right_end_pos}}
                                      ]},
                                      {"$and": [
                                          {"leftEndPosition": {"$gte": left_end_pos, "$lte": right_end_pos}},
                                          {"rightEndPosition": {"$gt": right_end_pos}}
                                      ]},
                                      {"$and": [
                                          {"leftEndPosition": {"$lte": left_end_pos}},
                                          {"rightEndPosition": {"$gte": right_end_pos}}
                                      ]}
                                    ]})
    closest_genes = []
    for gene in genes:
        if gene.strand == "forward":
            if abs(gene.left_end_position - central_pos) < max_distance:
                closest_genes.append(gene)
        elif gene.strand == "reverse":
            if abs(gene.right_end_position - central_pos) < max_distance:
                closest_genes.append(gene)
    return closest_genes


def find_by_bnumber(bnumber: str) -> Genes:
    return Genes.objects(bnumber=bnumber)


def find_by_bnumbers(bnumbers: [str]) -> [Genes]:
    return Genes.objects().filter(bnumber__in=bnumbers)


def get_id_by_bnumbers(bnumbers: [str]) -> [Genes]:
    genes = Genes.objects().filter(bnumber__in=bnumbers).only("id").only("bnumber")
    gene_bnumber = {}
    for gene in genes:
        gene_bnumber[gene.bnumber] = gene.id
    return gene_bnumber


def get_all_gene_product_relationships():
    results = Genes.objects().aggregate(*[{
        '$lookup': {
            'from': "product",
            'localField': '_id',
            'foreignField': 'gene_id',
            'as': 'products'
        }
    }])
    return results


def get_gene_motifs_relationship():
    results = Genes.objects().aggregate(*[{
        '$lookup': {
            'from': "product",
            'localField': '_id',
            'foreignField': 'gene_id',
            'as': 'products'
        }},
        # {"$unwind": "$products"},
        {"$lookup": {
            "from": "motif",
            "localField": "products._id",
            "foreignField": "products_id",
            "as": "motifs"
        }},
        # {"$unwind": "$motifs"},
        {"$project": {"_id": 1, "name": 1, "products._id": 1, "products.name": 1, "motifs._id": 1, "motifs.sequence": 1}},
        {"$count": "passing_scores"}
    ])
    return results

