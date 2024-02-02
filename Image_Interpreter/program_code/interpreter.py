import os
from google.cloud import vision


def interpret(filename):
    file = open('application_credentials.txt', 'r')
    credentials = file.readline()
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials
    curr_dir = os.path.dirname(__file__)
    top_dir = os.path.abspath((os.path.join(curr_dir, '..')))



    image_folder = os.fsencode(os.path.join(top_dir, "image_downloads"))
    def localize_objects(path):


        client = vision.ImageAnnotatorClient()

        with open(path, "rb") as image_file:
            content = image_file.read()
        image = vision.Image(content=content)

        objects = client.object_localization(image=image).localized_object_annotations
        num_objects = len(objects)
        output_string = " Image that displays: "



        #output_string = f"Number of objects found: {str(len(objects))}"

        for i in range(0,num_objects):
            if len(objects) == 1:
                output_string += f"{objects[i].name}."
                break
            elif i == len(objects) - 2 :
                output_string += f"{objects[i].name} and {objects[i+1].name}."
                break
            else:
                output_string += f"{objects[i].name}, "



            #print("(confidence: {str(object_.score)})")\

            #print("Normalized bounding polygon vertices: ")
            #for vertex in object_.bounding_poly.normalized_vertices:
                #print(f" - ({vertex.x}, {vertex.y})")
        return output_string







    result = localize_objects(os.path.join(top_dir,filename))

    def detect_landmarks(path):
        """Detects landmarks in the file."""


        client = vision.ImageAnnotatorClient()

        with open(path, "rb") as image_file:
            content = image_file.read()

        image = vision.Image(content=content)


        response = client.landmark_detection(image=image)
        landmarks = response.landmark_annotations
        print("Landmarks:")
        num_of_landmarks = len(landmarks)
        print('num of landmarks',str(num_of_landmarks))


        for landmark in landmarks:
            print(landmark.description)
            for location in landmark.locations:
                lat_lng = location.lat_lng
                print(f"Latitude {lat_lng.latitude}")
                print(f"Longitude {lat_lng.longitude}")

        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )
        return num_of_landmarks
    return result


    # for file in os.listdir(image_folder):
    #     print(os.path.join(image_folder, file))
    #     detect_landmarks(os.path.join(image_folder,file))






    # def get_lables():
    #
    #
    #     def get_labels(path):
    #
    #         from google.cloud import vision
    #
    #         client = vision.ImageAnnotatorClient()
    #
    #         with open(path, "rb") as image_file:
    #             content = image_file.read()
    #
    #         image = vision.Image(content=content)
    #
    #         response = client.label_detection(image=image)
    #         labels = response.label_annotations
    #         print("Labels:")
    #
    #         for label in labels:
    #             print(label.description)
    #
    #         if response.error.message:
    #             raise Exception(
    #                 "{}\nFor more info on error messages, check: "
    #                 "https://cloud.google.com/apis/design/errors".format(response.error.message)
    #             )
    #
    #
    #
    #
    #     for file in os.listdir(image_folder):
    #         print(os.path.join(image_folder, file))
    #         get_labels(os.path.join(image_folder, file))


