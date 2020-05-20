#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

import os
import sys
import traceback
import codecs
import re


class FormSet:
    pass

    def __init__(self):
        self.forms = []

    def add_form(self, form):
        self.forms.append(form)


class Form:
    pass

    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.subforms = []
        self.items = []
        #print('[ %s ]' % (self.title))

    def __str__(self):
        return '''
submenu "%s" {
    %s
    %s
    sleep 0
}
        ''' % (self.title.replace('"', '\\"'), ''.join([x.to_script() for x in self.subforms]), ''.join([x.to_script() for x in self.items]))

    def to_script(self):
        return self.__str__()
    
    def to_file(self):
        with codecs.open('./%s.cfg' % (self.id), 'w', encoding='utf-8') as out:
            for f in self.subforms:
                f.to_file()
                out.write('''
submenu "%s" {
    configfile $prefix/%s.cfg
}
                ''' % (f.title.replace('"', '\\"'), f.id))
            for i in self.items:
                out.write(i.to_script())

    def add_item(self, item):
        self.items.append(item)

    def add_subforms(self, form):
        self.subforms.append(form)


class Item:
    pass

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.options = []
        #print('\t >> %s' % (self.name))

    def __str__(self):
        return '''
submenu "%s" {
    %s
    sleep 0
}
        ''' % (self.name.replace('"', '\\"'), ''.join([x.to_script() for x in self.options]))

    def to_script(self):
        return self.__str__()

    def add_option(self, option):
        self.options.append(option)


class Option:
    pass

    def __init__(self, name, value, default=False):
        self.name = name
        self.value = value
        self.default = default
        #print('\t\t -- %s = %s (%s)' % (self.name, self.value, self.default))

    def __str__(self):
        return '''
submenu "%s%s" {
    echo %s
}
        ''' % (self.name.replace('"', '\\"'), ' (default)' if self.default else '', self.value)

    def to_script(self):
        return self.__str__()

    def set_addr(self, addr):
        self.addr = addr


if __name__ == '__main__':
    with codecs.open('./_Setup/setup_extr.txt', 'r', encoding='cp437') as txt:
        contents = []
        contents = txt.readlines()
        # for idx1 in range(0, len(contents)):
        #     contents[idx1] = contents[idx1].decode('cp437')
        #     print(contents[idx1])
        formset = {}
        refs = {}
        stacks = []
        for idx1 in range(0, len(contents)):
            if contents[idx1][8:].strip().startswith('Form Set:'):
                stacks.append(idx1)
            elif contents[idx1][8:].strip().startswith('Form:'):
                stacks.append(idx1)
            elif contents[idx1][8:].strip().startswith('End Form Set'):
                idx0 = stacks.pop()
                print('Form Set ', idx0, idx1)
            elif contents[idx1][8:].strip().startswith('End Form'):
                idx0 = stacks.pop()
                print('Form ', idx0, idx1)
                form = None
                try:
                    regx = re.compile('^Form: (.+?), FormId: (.+?) \{.+\}$')
                    vals = regx.findall(contents[idx0][8:].strip())[0]
                    form = Form(id=vals[1], title=vals[0])
                    if refs.has_key(vals[1]):
                        refs[vals[1]].add_subforms(form)
                    else:
                        formset[vals[1]] = form
                except:
                    continue
                if form is None:
                    continue
                if idx1 - idx0 > 1:
                    item = None
                    for line in contents[idx0+1:idx1]:
                        if line[8:].strip().startswith('One Of:'):
                            item = None
                            option = None
                            try:
                                regx = re.compile(
                                    '^One Of: (.+?), VarStoreInfo \(VarOffset/VarName\): (.+?), VarStore: (.+?), QuestionId: (.+?), Size: (.+?), Min: (.+?), Max (.+?), Step: (.+?) \{.+\}$')
                                vals = regx.findall(line[8:].strip())[0]
                                item = Item(name=vals[0], addr=vals[2])
                                form.add_item(item)
                            except:
                                continue
                        elif line[8:].strip().startswith('One Of Option:'):
                            option = None
                            if item is None:
                                continue
                            try:
                                regx = re.compile(
                                    '^One Of Option: (.+?), Value \((.+?) bit\): (.+?) (\(default.*?\))?[ ]?\{.+\}$')
                                vals = regx.findall(line[8:].strip())[0]
                                option = Option(name=vals[0], value=vals[2], default=(len(vals[3]) > 0))
                                item.add_option(option)
                            except:
                                continue
                        elif line[8:].strip().startswith('End One Of'):
                            item = None
                            option = None
                        elif line[8:].strip().startswith('Ref:'):
                            item = None
                            option = None
                            try:
                                regx = re.compile(
                                    '^Ref: (.+?), VarStoreInfo \(VarOffset/VarName\): (.+?), VarStore: (.+?), QuestionId: (.+?), FormId: (.+?) \{.+\}')
                                vals = regx.findall(line[8:].strip())[0]
                                if formset.has_key(vals[4]):
                                    form.add_subforms(formset.pop(vals[4]))
                                else:
                                    refs[vals[4]] = form
                            except:
                                continue
    with codecs.open('./grub.cfg', 'w', encoding='utf-8') as out:
        for form in formset.values():
            out.write(form.to_script())

    for form in formset.values():
        form.to_file()
    with codecs.open('./grub.cfg', 'w', encoding='utf-8') as out:
        for form in formset.values():
            out.write('''
menuentry "%s" {
    configfile $prefix/%s.cfg
}
            ''' % (form.title, form.id))
