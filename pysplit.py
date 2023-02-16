#! /usr/bin/python3
```
  -*- coding: utf-8 -*-
  -*- version: python3 -*-
  -*- author: Xb -*-
  -*- Date: 2023/2/16 -*-
  -*- email: qianxiaobo@genomics.cn -*-
```


import sys, os
import argparse as ag

parser = ag.ArgumentParser(prog='pysplit', description='split files by lines or number of files')

parser.add_argument('file')

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-l', dest='lines', help='the lines for each splitted file', type=int)
group.add_argument('-n', dest='number', help='the number of files to split', type=int)
parser.add_argument('-o', '--out', default='xx', help='prefix for splitted files', required=True)
parser.add_argument('--suffix', help='sufix for splitted files')
args = parser.parse_args()
with open(args.file, 'r') as fin:
	ls = fin.readlines()
	all_ls = len(ls)
	print(all_ls)
	print(args.lines)
	if args.lines:
		n = args.lines
		nfiles = all_ls//n + 1
	if args.number:
		nfiles = args.number
		n = all_ls // nfiles + 1
	for i in range(0, nfiles):
		if args.suffix:
			outname = args.out + str(i+1) + '.' + args.suffix
		else:
			outname = args.out + str(i+1)
		with open(outname, 'w') as fout:
			start = i*n
			end = min(((i+1)*n - 1), (all_ls - 1)) + 1
			new_ls = ls[start:end]
			for j in new_ls:
				print(j.strip(), file=fout)
