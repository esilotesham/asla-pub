"""
Class to invoke update_service
"""
from predict_service import PredictService


def main():
    predict_service = PredictService()
    for i in range(100):
        predict_service.capture_gesture()
        label = predict_service.predict_label()
        print label

if __name__ == "__main__":
    main()
