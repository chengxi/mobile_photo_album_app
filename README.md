A basic android app of mobile photo album and server side 

Prompt used to generate the whole package. 

>Context: We are creating a prototype that can run locally. The server side will be accessible from localhost. The client/app is android only and will be running on an android device emulator only. We don’t plan to deploy server side service to the cloud and we don’t plan to publish the app to google play. Let’s keep things simple and make local version work. At each major step, explain the decision/plan/decision and some technical details before execution. 
>
>Task: Develop a personal photo album mobile app (called ‘Photo Album Mobile App’) where user can upload photos from mobile device and view it in the albums that are local as well as from server side. In this task, create a prototype version that can be fully set up on local machine but leave comments about how to deploy it to cloud and google play and apple App Store.
>

Some quirks: 
- The mobile app code were quite straightforward, the main headache is resolving build errors such as Gradle failures.

Steps to run
- client side: Use Android studio to set up a running virtual device and then run `flutter run` inside the client folder
- server side is simpler: set up venv: source venv/bin/activate, then python app.py
