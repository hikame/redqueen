/* 
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
*/

#pragma once

#include "qemu/osdep.h"
#include <linux/kvm.h>

void synchronization_check_reload_pending(CPUState *cpu);
void synchronization_unlock(void);
void synchronization_lock(CPUState *cpu);
void synchronization_reload_vm(void);
void synchronization_disable_pt(CPUState *cpu);
