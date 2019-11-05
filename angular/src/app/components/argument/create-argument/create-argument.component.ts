import { Component, OnInit } from '@angular/core';

import { ArgumentService } from 'src/app/services/argument/argument.service';
import { Argument } from '../argument';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-create-argument',
  templateUrl: './create-argument.component.html',
  styleUrls: ['./create-argument.component.css']
})
export class CreateArgumentComponent implements OnInit {
  private form: FormGroup;
  private argument: Argument;

  title = new FormControl('', Validators.required);
  content = new FormControl('', Validators.required);
  user_id = new FormControl('', Validators.required);
  debate_id = new FormControl('', Validators.required);

  constructor(
    public service: ArgumentService,
    private fb: FormBuilder
  ) {
    this.form = fb.group({
      'title': this.title,
      'content': this.content,
      'user_id': this.user_id,
      'debate_id': this.debate_id
    });
  }

  ngOnInit() {
  }

  onSubmit() {
    this.argument = new Argument(
      this.form.value.title,
      this.form.value.content,
      this.form.value.user_id,
      this.form.value.debate_id
      );
    this.service.createArgument(this.argument).subscribe(
      data => {
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
  }
}
