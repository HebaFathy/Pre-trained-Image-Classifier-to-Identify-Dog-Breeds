# Pre-trained-Image-Classifier-to-Identify-Dog-Breeds

## Tasks:

Using  Python skills, we determined which image classification algorithm works the "best" on classifying images as "dogs" or "not dogs". The Input is an image. The output determines what the image depicts. (for example, a dog). Be mindful of the fact that image classifiers do not always categorize the images correctly.

Timed how long each algorithm takes to solve the classification problem. With computational tasks, there is often a trade-off between accuracy and runtime. The more accurate an algorithm, the higher the likelihood that it will take more time to run and use more computational resources to run.


## Results:

We provided the results from running the check_images.py for all three CNN model architectures. 

Compared these results to the ones your program produced when you ran run_models_batch.sh (or run_models_batch_hints.sh) in the Printing Results section.

## Main objectives:

Identifying which pet images are of dogs and which pet images aren't of dogs

Classifying the breeds of dogs, for the images that are of dogs.

For objective 1, notice that both VGG and AlexNet correctly identify images of "dogs" and "not-a-dog" 100% of the time.

For objective 2, VGG provides the best solution because it classifies the correct breed of dog over 90% of the time.
Results Table

## Project Results

Given our results, the "best" model architecture is VGG. It outperformed both of the other architectures when considering both objectives 1 and 2. We noticed that ResNet did classify dog breeds better than AlexNet, but only VGG and AlexNet were able to classify "dogs" and "not-a-dog" at 100% accuracy. The model VGG was the one that was able to classify "dogs" and "not-a-dog" with 100% accuracy and had the best performance regarding breed classification with 93.3% accuracy.
