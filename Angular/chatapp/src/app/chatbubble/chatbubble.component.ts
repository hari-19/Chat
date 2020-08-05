import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-chatbubble',
  templateUrl: './chatbubble.component.html',
  styleUrls: ['./chatbubble.component.scss']
})
export class ChatbubbleComponent implements OnInit {

  @Input() isSelf:boolean=true;
  @Input() text:string;
  @Input() image:string = "../../assets/profile_placeholder.png";

  constructor() { }

  ngOnInit(): void {
  }

}
