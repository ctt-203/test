#!/usr/bin/env python
# coding: utf-8

import requests, bs4, graphviz

class PEPEntry:
    def __init__(self, status, ID, title, href, authors, versions):
        self.status = status
        self.ID = ID
        self.title = title
        self.href = href
        self.created = self.extract_date(href)
        self.authors = self.split_authors(authors)
        self.versions = versions

    def split_authors(self, authors):
        if not authors:
            return []
        else:
            authors = authors.replace(", Jr.", " Jr.")
            return authors.split(", ")

    def extract_date(self, href):
        prefix = "https://peps.python.org/numerical"
        url = f"{prefix}/{href}"
        res = requests.get(url)
        if res.status_code != 200:
            return ""
        dom = bs4.BeautifulSoup(res.text)
        created = dom.find(string="Created")
        if created:
            date = created.find_next("dd").get_text()
            return date
        else:
            return ""


if __name__ == "__main__":
    res = requests.get("https://peps.python.org/numerical/")
    if res.status_code == 200:
        dom = bs4.BeautifulSoup(res.text)
        entries = []
        for tr in dom.find("table").find("tbody").find_all("tr")[:10]:
            tds = tr.find_all("td")
            if len(tds) < 5:
                continue
            status = tds[0].get_text()
            ID = tds[1].get_text()
            title = tds[2].get_text()
            href = tds[2].find("a").get("href")
            authors = tds[3].get_text()
            versions = tds[4].get_text()
            entry = PEPEntry(status, ID, title, href, authors, versions)
            entries.append(entry)

        graph = graphviz.Graph()
        edge_set = set()
        for entry in entries:
            length = len(entry.authors)
            for i in range(length):
                a1 = entry.authors[i]
                for j in range(i+1, length):
                    a2 = entry.authors[j]
                    edge = (a1, a2)
                    if (a1, a2) in edge_set or (a2, a1) in edge_set:
                        continue
                    else:
                        graph.edge(a1, a2)
                        edge_set.add((a1, a2))

        print(graph.source)



        

