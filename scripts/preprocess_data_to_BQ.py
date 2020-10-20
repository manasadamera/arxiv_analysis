#!/usr/bin/env python
# coding: utf-8
import json


def modify_authors_parsed():
    author_names = ["last_name", "middle_name", "suffix"]
    with open("data/arxiv-metadata-oai-snapshot_modified.json", 'w') as fw:
        with open("data/arxiv-metadata-oai-snapshot.json", 'r') as fr:
            for line in fr.readlines():
                row = json.loads(line)
                authors_parsed = row["authors_parsed"]
                authors_parsed_modified = [dict(zip(author_names, author)) for author in authors_parsed]
                row["authors_parsed"] = authors_parsed_modified
                json.dump(row, fw)
                fw.write("\n")


if __name__ == '__main__':
    modify_authors_parsed()




