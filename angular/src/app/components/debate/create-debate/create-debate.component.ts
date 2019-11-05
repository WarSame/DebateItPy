import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Debate } from '../debate';
import { DebateService } from 'src/app/services/debate/debate.service';

@Component({
  selector: 'app-create-debate',
  templateUrl: './create-debate.component.html',
  styleUrls: ['./create-debate.component.css']
})
export class CreateDebateComponent implements OnInit {
  private form: FormGroup;
  private debate: Debate;

  title = new FormControl('', Validators.required);
  description = new FormControl('', Validators.required);
  creator_id = new FormControl('', Validators.required);
  community_id = new FormControl('', Validators.required);

  constructor(
    public service: DebateService,
    private fb: FormBuilder
  ) {
    this.form = fb.group({
      'title': this.title,
      'description': this.description,
      'creator_id': this.creator_id,
      'community_id': this.community_id
    });
  }

  ngOnInit() {
  }

  onSubmit() {
    this.debate = new Debate(
      this.form.value.title,
      this.form.value.description,
      this.form.value.creator_id,
      this.form.value.community_id
      );
    this.service.createDebate(this.debate).subscribe(
      data => {
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
  }

}
