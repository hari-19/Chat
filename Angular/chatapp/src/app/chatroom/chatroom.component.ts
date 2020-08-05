import { Component, OnInit } from '@angular/core';
import {faPaperPlane} from '@fortawesome/free-regular-svg-icons';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

@Component({
  selector: 'app-chatroom',
  templateUrl: './chatroom.component.html',
  styleUrls: ['./chatroom.component.scss']
})
export class ChatroomComponent implements OnInit {

  faPaperPlane = faPaperPlane;

  messages = [
    {
      text:"Hi",
      isSelf:false
    },
    {
      text:"Hi",
      isSelf:true
    },
    {
      text:"How are youasdfassssssssas asdfas df asd fas df asd fas df as dfa sdf as df asd sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
      isSelf:false
    },
    {
      text:"I am fine",
      isSelf:true
    },
    {
      text:"This is a perfect App",
      isSelf:false
    },
  ]

  constructor() { }

  ngOnInit(): void {
  }

}
