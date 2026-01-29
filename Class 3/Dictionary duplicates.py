student_data = {'id1':
    {'name' : ['sarah'],
     'class' : ['V'],
     'subject_integaration' : ['maths', 'science', 'english']
    },
    'id2':
    {'name' : ['john'],
     'class' : ['V'],
     'subject_integaration' : ['maths', 'science', 'english']
    },
    'id3':
    {'name' : ['sarah'],
     'class' : ['V'],
     'subject_integaration' : ['maths', 'science', 'english']
    },
    'id4':
    {'name' : ['emma'],
     'class' : ['V'],
     'subject_integaration' : ['maths', 'science', 'english']
    },
}
result = {}
for key, value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)