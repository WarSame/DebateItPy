import { Component, OnInit } from '@angular/core';

import { ArgumentService } from 'src/app/services/argument/argument.service';
import { Argument } from '../argument';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-create-post',
  templateUrl: './create-post.component.html',
  styleUrls: ['./create-post.component.css']
})
export class CreateArgumentComponent implements OnInit {
  private form: FormGroup;
  private argument: Argument;

  title = new FormControl('', Validators.required);
  text = new FormControl('', Validators.required);
  user_id = new FormControl('', Validators.required);
  debate_id = new FormControl('', Validators.required);

  constructor(
    public service: ArgumentService,
    private fb: FormBuilder
  ) {
    this.form = fb.group({
      'title': this.title,
      'text': this.text,
      'user_id': this.user_id,
      'debate_id': this.debate_id
    });
  }

  ngOnInit() {
  }

  onSubmit() {
    this.argument = new Argument(
      this.form.value.title,
      this.form.value.text,
      this.form.value.user_id,
      this.form.value.debate_id
      );
    this.service.createPost(this.argument).subscribe(
      data => {
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
  }
}
