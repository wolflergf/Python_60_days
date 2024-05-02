contents = [
    "All carrots are to be sliced longitudinally.",
    "The carrots were reportedly sliced",
    "The slicing process was well presented.",
]

file_names = ["doc.txt", "report.txt", "presentation.txt"]


for content, file_name in zip(contents, file_names):
    file = open(f"./{file_name}", "w")
    file.write(content)
