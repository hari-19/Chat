import { Component, OnInit, AfterViewInit } from '@angular/core';
import {faPaperPlane} from '@fortawesome/free-regular-svg-icons';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

@Component({
  selector: 'app-chatroom',
  templateUrl: './chatroom.component.html',
  styleUrls: ['./chatroom.component.scss']
})
export class ChatroomComponent implements OnInit, AfterViewInit {

  faPaperPlane = faPaperPlane;
  container:HTMLElement;

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

  ngAfterViewInit() {         
    this.container = document.getElementById("message-box");           
    this.container.scrollTop = this.container.scrollHeight;     
  }  

}
