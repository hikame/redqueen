#!/bin/bash
# 
# This file is part of Redqueen.
#
# Sergej Schumilo, 2019 <sergej@schumilo.de> 
# Cornelius Aschermann, 2019 <cornelius.aschermann@rub.de> 
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Redqueen.  If not, see <http://www.gnu.org/licenses/>.
#
if [[ "$OSTYPE" == "linux-gnu" ]]; then

	mkdir bin/ 2> /dev/null
	mkdir bin/loader/ 2> /dev/null
	mkdir bin/fuzzer/ 2> /dev/null
	mkdir bin/info/ 2> /dev/null

	printf "\tCompiling loader...\n"
	gcc src/loader/loader.c  -static -I ../ -o bin/loader/loader
	printf "\tCompiling stage 2 loader...\n"
    gcc -c -O0 src/loader/stage2_loader.c -I ../ -o bin/loader/stage2_loader.o
	printf "\tCompiling info executable...\n"
	gcc -static src/info/info.c -I ../ -o bin/info/info
	printf "\tCompiling vuln_driver fuzzer...\n"
	gcc src/fuzzer/kafl_vuln_test.c -I ../ -o bin/fuzzer/kafl_vuln_test
	printf "\tCompiling kafl_vuln_json test...\n"	
	gcc src/fuzzer/kafl_vuln_json.c -I ../ -o bin/fuzzer/kafl_vuln_json
    printf "\tCompiling hprintf test...\n"
	gcc src/fuzzer/hprintf_test.c -I ../ -o bin/fuzzer/hprintf_test
	printf "\tCompiling EXT4 fuzzer...\n"
	gcc src/fuzzer/fs_fuzzer.c -I ../ -o bin/fuzzer/ext4 -D EXT4
	printf "\tCompiling NTFS fuzzer...\n"
	gcc src/fuzzer/fs_fuzzer.c -I ../ -o bin/fuzzer/ntfs -D NTFS
	printf "\tCompiling VFAT fuzzer...\n"
	gcc src/fuzzer/fs_fuzzer.c -I ../ -o bin/fuzzer/vfat -D VFAT
	printf "\tCompiling BTRFS fuzzer...\n"
	gcc src/fuzzer/fs_fuzzer.c -I ../ -o bin/fuzzer/btrfs -D BTRFS
	printf "\tCompiling XFS fuzzer...\n"
	gcc src/fuzzer/fs_fuzzer.c -I ../ -o bin/fuzzer/xfs -D XFS
	printf "\tCompiling HFS fuzzer...\n"
	gcc src/fuzzer/fs_fuzzer.c -I ../ -o bin/fuzzer/hfs -D HFS
    printf "\tCompiling HFSPLUS fuzzer...\n"
    gcc src/fuzzer/fs_fuzzer.c -I ../ -o bin/fuzzer/hfsplus -D HFSPLUS
	printf "\tCompiling ISOFS fuzzer...\n"
	gcc src/fuzzer/fs_fuzzer.c -I ../ -o bin/fuzzer/isofs -D ISOFS
	printf "\tCompiling QNX fuzzer...\n"
	gcc src/fuzzer/fs_fuzzer.c -I ../ -o bin/fuzzer/qnx -D QNX
	printf "\tCompiling FAT fuzzer...\n"
	gcc src/fuzzer/fs_fuzzer.c -I ../ -o bin/fuzzer/fat -D FAT
	printf "\tCompiling JFS fuzzer...\n"
	gcc src/fuzzer/fs_fuzzer.c -I ../ -o bin/fuzzer/jfs -D JFS
	printf "\tCompiling GFS2 fuzzer...\n"
	gcc src/fuzzer/fs_fuzzer.c -I ../ -o bin/fuzzer/gfs2 -D GFS2
	printf "\tCompiling GFS2META fuzzer...\n"
	gcc src/fuzzer/fs_fuzzer.c -I ../ -o bin/fuzzer/gfs2meta -D GFS2META
	printf "\tCompiling REISERFS fuzzer...\n"
	gcc src/fuzzer/fs_fuzzer.c -I ../ -o bin/fuzzer/reiserfs -D REISERFS
else
	printf "\tError: Cannont compile linux userspace components on this plattform!\n\tPlease use Linux instead!\n"
fi
