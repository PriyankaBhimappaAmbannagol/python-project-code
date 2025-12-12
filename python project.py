faqs={
    "college timings": "college timings are from 8:00 AM to 4:45 PM.",
    "minimum percentage of attendance required for final exams": "minimum 75% of attendance is required.",
    "how to apply for leave": "You can apply for leave leave from college portal or by writing leave letter.",
    "fees payment last date":"last date for fees payment has been displayed on the notice board.",
    " how about exam schedule": "exams are conducted at the end of each semister.",
    "how is the teaching": "teaching is quite good actually."
    }
print("Simple FAQ Assistant")
print("Ask a question ")
print("--------------------------------\n")
while True:
    question=input("You:").lower()

    if question == "exit":
       print("Assistsnt: Thank You! Bye")
       break
    found=False
    for key in faqs:
      if key in question:
        print("Assistant:",faqs[key])
        found=True
        break
    if not found:
        print("Assistant: sorry,I don't have an answer for that")
    
