import 'dart:io';

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({
    Key? key,
    required this.title,
  }) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final picker = ImagePicker();
  XFile? imageFile;

  Future getImage(int type) async {
    XFile? image = await picker.pickImage(
        source: type == 1 ? ImageSource.camera : ImageSource.gallery);
    return image;
  }

  Widget buildElevatedButton(String buttonText, int imgOption) {
    return ElevatedButton(
      style: ElevatedButton.styleFrom(
        padding: const EdgeInsets.all(15),
        primary: Colors.black,
        onPrimary: Colors.white,
        textStyle: const TextStyle(
          fontSize: 12,
          fontWeight: FontWeight.bold,
        ),
      ),
      onPressed: () async {
        imageFile = await getImage(imgOption);
        setState(() {});
      },
      child: Text(buttonText),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey,
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Column(
        children: [
          Image.asset(, width: 224, height: 224,),
          const SizedBox(
            height: 50,
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              buildElevatedButton('PICK FROM GALLERY', 2),
              buildElevatedButton('PICK FROM CAMERA', 1),
            ],
          )
        ],
      ),
    );
  }
}

// Container(
//             width: 230,
//             height: 230,
//             margin: const EdgeInsets.all(75),
//             decoration: BoxDecoration(
//               border: Border.all(
//                 width: 6,
//                 color: Colors.white,
//               ),
//               image: DecorationImage(
//                 image: imageFile != null
//                     ? FileImage(File(imageFile!.path))
//                     : const AssetImage('assets/images/wp3439728.jpg')
//                         as ImageProvider,
//                 fit: BoxFit.cover,
//               ),
//             ),
//           ),
