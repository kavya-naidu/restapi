from flask import Flask,jsonify


todo=Flask('__name__')

students=[
        {
            'std_id':1,
            'student_name':'aslam',
            'age':21,
            'email':'aslam262004@gmail.com'
        },
        {
            'std_id':2,
            'student_name': 'rakshitha',
            'age': 20,
            'email': 'rakshitha2735@gmail.com'
        },
        {
            'std_id':3,
            'student_name': 'padmashree',
            'age': 21,
            'email': 'padmashree22004@gmail.com'
        },
        {
            'std_id':4,
            'student_name': 'sami',
            'age': 20,
            'email': 'sami@gmail.com'
        },
        {
            'std_id':5,
            'student_name': 'aslam',
            'age': 21,
            'email': 'aslam262004@gmail.com'
        },

    ]

@todo.route('/students-list')
def student_list():
    return jsonify(students)

@todo.route('/student/get/<int:std_id>')
def student_get_by_id(std_id):
    for std in students:
        if std['std_id']==std_id:
            return jsonify(std)
    return "id not found"





if __name__ == '__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )
