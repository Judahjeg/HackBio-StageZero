#Phenylalanine Team Assignment 
import requests

#This will fetch gene DNA from NCBI using accession number
def fetch_gene_sequence(accession):
    url = f"https://ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id={accession}&db=nuccore&report=fasta&retmode=text"
    response = requests.get(url)
    return response.text



team = [
    {
        "name": "Svetlana",
        "slack": "Svetlana Sokolova",
        "country": "United Kingdom",
        "hobby": "Playing piano",
        "affiliation": "Queen’s University Belfast",
        "gene": "TP53",
        "accession": "NM_000546"   # TP53 gene accession
    },
    {
        "name": "Santosh Timilsina",
        "slack": "Santosh T",
        "country": "United States of America",
        "hobby": "Tennis",
        "affiliation": "University of Texas at San Antonio",
        "gene": "IFNB1",
        "accession": "NM_002176"   # IFNB gene
    },
    {
        "name": "Gideon Danso",
        "slack": "Joegidi4real",
        "country": "Ghana",
        "hobby": "Listening to music",
        "affiliation": "University of Cape Coast",
        "gene": "BRCA2",
        "accession": "NM_000059"   # BRCA2 gene
    },
    {
        "name": "Mosunmola Temitope Christianah",
        "slack": "Temmy",
        "country": "Nigeria",
        "hobby": "Cooking",
        "affiliation": "Obafemi Awolowo University",
        "gene": "TNNT2",
        "accession": "NM_001001430"  # TNNT2 gene
    },
    {
        "name": "Hana E",
        "slack": "Hana E",
        "country": "Canada",
        "hobby": "Hiking",
        "affiliation": "Boise State University",
        "gene": "glnD",
        "accession": "AF002837"   # glnD gene (example bacterial gene)
    },
    {
        "name": "Jegede Judah Olayemi",
        "slack": "Jegede Judah",
        "country": "Nigeria",
        "hobby": "Playing Soccer",
        "affiliation": "Obafemi Awolowo University",
        "gene": "POSTN",
        "accession": "NM_001330358"  # POSTN gene
    }
]



#We are Printing the team info and DNA
for person in team:
    print("Name:", person["name"])
    print("Slack username:", person["slack"])
    print("Country:", person["country"])
    print("Hobby:", person["hobby"])
    print("Affiliation:", person["affiliation"])
    print("Favorite gene:", person["gene"])
    
    dna = fetch_gene_sequence(person["accession"])
    print("DNA sequence:")
    print(dna[:200], "...")  # print only first 200 letters to keep output short
    
    print("-" * 60)
