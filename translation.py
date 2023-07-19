#!/usr/bin/env python
# coding: utf-8

# In[22]:


import json
import sys


# In[23]:




# In[24]:


def parse_expression(expr):
    try:
        if expr['type'] == 'BinaryExpression':
            left = parse_expression(expr['left'])
            operator = expr['operator']
            right = parse_expression(expr['right'])
            return f'({left} {operator} {right})'
        elif expr['type'] == 'MemberExpression':
            var_name = ""
            while expr['type'] == 'MemberExpression':
                if expr['property']['type'] == 'Identifier':
                    var_name = f"{expr['property']['name']}.{var_name}"
                expr = expr['object']
            return var_name.rstrip('.')
        elif expr['type'] == 'Identifier':
            return expr['name']
        elif expr['type'] == 'Literal':
            return str(expr['value'])
        elif expr['type'] == 'CallExpression' and expr['callee']['type'] == 'MemberExpression' and expr['callee']['object']['type'] == 'ThisExpression' and expr['callee']['property']['type'] == 'Identifier' and expr['callee']['property']['name'] == 'compare':
            args = [parse_expression(arg) for arg in expr['arguments']]
            return f'({args[0]} < {args[1]})'  # assuming all compares are for less than
        else:
            raise Exception(f'Unsupported expression type: {expr["type"]}')
    except KeyError as e:
        print(f"KeyError: {str(e)}")
        print(f"expr: {json.dumps(expr, indent=2)}")
        raise


# In[25]:


def parse_block(block):
    for stmt in block:
        parse_statement(stmt)


# In[26]:


def parse_statement(stmt):
    if stmt['type'] == 'VariableDeclaration':
        for decl in stmt['declarations']:
            if decl['init'] is None:
                print(f'VAR {decl["id"]["name"]}: INT; // assuming INT type by default')
            else:
                print(f'VAR {decl["id"]["name"]}: INT := {parse_expression(decl["init"])};')
    elif stmt['type'] == 'ExpressionStatement':
        expr = stmt['expression']
        if expr['type'] == 'AssignmentExpression':
            left = parse_expression(expr['left'])
            right = parse_expression(expr['right'])
            print(f'{left} := {right};')
    elif stmt['type'] == 'IfStatement':
        test = parse_expression(stmt['test'])
        print(f'IF {test} THEN')
        parse_block(stmt['consequent']['body'])
        if stmt['alternate'] is not None:
            print('ELSE')
            if stmt['alternate']['type'] == 'BlockStatement':
                parse_block(stmt['alternate']['body'])
            else:  # a single statement, not a block
                parse_statement(stmt['alternate'])
        print('END_IF')
    else:
        raise Exception(f'Unsupported statement type: {stmt["type"]}')


def parse_code(block):
    with open('mainCode.scl', 'w') as f:
        sys.stdout = f
        parse_block(block)
        sys.stdout = sys.__stdout__


# In[27]:

if __name__ == '__main__':
    # load the AST
    with open('ast.json') as f:
        ast = json.load(f)

    parse_block(ast['body'])

