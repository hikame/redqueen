"""
This file is part of the Redqueen fuzzer.

Sergej Schumilo, 2019 <sergej@schumilo.de> 
Cornelius Aschermann, 2019 <cornelius.aschermann@rub.de> 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with Redqueen.  If not, see <http://www.gnu.org/licenses/>. 
"""

ACQUIRE									=	'R'
RELEASE									=	'D'

RELOAD									=	'L'
ENABLE_SAMPLING							=	'S'
DISABLE_SAMPLING						=	'O'
COMMIT_FILTER							=	'T'
FINALIZE								=	'F'

ENABLE_RQI_MODE							=	'A'
DISABLE_RQI_MODE						=	'B'
ENABLE_TRACE_MODE						=	'E'
DISABLE_TRACE_MODE						=	'G'
ENABLE_PATCHES							=	'P'
DISABLE_PATCHES							=	'Q'
REDQUEEN_SET_LIGHT_INSTRUMENTATION		=	'U'
REDQUEEN_SET_SE_INSTRUMENTATION			=	'V'
REDQUEEN_SET_WHITELIST_INSTRUMENTATION	=	'W'
REDQUEEN_SET_BLACKLIST 					=	'X'

CRASH									=	'C'
KASAN									=	'K'
INFO									=	'I'
TIMEOUT									=	't'

PRINTF									=	'X'

PT_TRASHED								=	'Z'
PT_TRASHED_CRASH						=	'M'
PT_TRASHED_KASAN						=	'N'

ABORT									=	'H'



CMDS = {
    ACQUIRE									: "ACQUIRE",
    RELEASE									: "RELEASE",
    RELOAD									: "RELOAD",

    ENABLE_SAMPLING							: "ENABLE_SAMPLING",
    DISABLE_SAMPLING						: "DISABLE_SAMPLING",
    COMMIT_FILTER							: "COMMIT_FILTER",
    FINALIZE								: "FINALIZE",

	ENABLE_RQI_MODE							: "ENABLE_RQI_MODE",
    DISABLE_RQI_MODE						: "DISABLE_RQI_MODE",

    ENABLE_TRACE_MODE						: "ENABLE_TRACE_MODE",
	DISABLE_TRACE_MODE						: "DISABLE_TRACE_MODE",
	ENABLE_PATCHES							: "ENABLE_PATCHES",
	DISABLE_PATCHES							: "DISABLE_PATCHES",
	REDQUEEN_SET_LIGHT_INSTRUMENTATION		: "REDQUEEN_SET_LIGHT_INSTRUMENTATION",
	REDQUEEN_SET_SE_INSTRUMENTATION			: "REDQUEEN_SET_SE_INSTRUMENTATION",
	REDQUEEN_SET_WHITELIST_INSTRUMENTATION	: "REDQUEEN_SET_WHITELIST_INSTRUMENTATION",
	REDQUEEN_SET_BLACKLIST					: "REDQUEEN_SET_BLACKLIST",

	CRASH									: "CRASH",
	KASAN									: "KASAN",
	INFO									: "INFO",

	PRINTF									: "PRINTF",
	
	PT_TRASHED								: "PT_TRASHED",
	PT_TRASHED_CRASH						: "PT_TRASHED_CRASH",
	PT_TRASHED_KASAN						: "PT_TRASHED_KASAN",

	ABORT									: "ABORT",
}
