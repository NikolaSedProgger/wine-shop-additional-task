from random import choice
from datetime import timedelta, datetime
from docxtpl import DocxTemplate


def generate_object_shedule(object):
    date = datetime.strptime('8:00 AM', '%I:%M %p')
    start = date + timedelta(hours=0, minutes=choice(list(range(5, 35, 5))))
    start_date = f"{str((start).time())[:5]} {yesterday_date.date()}"
    object_shedule = {object: [start_date.replace('-', '.')]}
    delta_minutes = list(range(30, 65, 5))

    for time in range(13):
        delta_time = timedelta(hours=1, minutes=choice(delta_minutes))
        date = date + delta_time
        if int(str((date).time())[:2]) > 7:
            exit_date = f"{str((date).time())[:5]} {yesterday_date.date()}"
            exit_time = exit_date.replace('-', '.')
        else:
            exit_date = f"{str((date).time())[:5]} {today_date.date()}"
            exit_time = exit_date.replace('-', '.')
        object_shedule[object].append(exit_time)
    return object_shedule

def get_objects_list(file):
    with open(file, encoding="utf-8") as f:
        objects = [line.strip() for line in f]
    return objects

if __name__ == "__main__":
    objects = get_objects_list("objects.txt")

    today_date = datetime.now()
    delta = timedelta(days=1)
    yesterday_date = today_date - delta
    
    schedule = {}
    for object in objects:
        schedule.update(generate_object_shedule(object))
    path = "шаблон.docx"
    doc = DocxTemplate(path)
    context = {
        'date_begin': yesterday_date.date(),
        'date_end': today_date.date(),
        'schedule': schedule
    }
    doc.render(context)
    doc.save(f"{str(yesterday_date.date()).replace('-','.')}-{str(today_date.date()).replace('-','.')}.docx")
