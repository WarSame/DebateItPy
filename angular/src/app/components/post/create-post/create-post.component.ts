import { Component, OnInit } from '@angular/core';

import { PostService } from 'src/app/services/post/post.service';
import { Post } from '../post';
import { FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-create-post',
  templateUrl: './create-post.component.html',
  styleUrls: ['./create-post.component.css']
})
export class CreatePostComponent implements OnInit {
  private form: FormGroup;
  private post: Post;

  title = new FormControl('', Validators.required);
  text = new FormControl('', Validators.required);
  user_id = new FormControl('', Validators.required);
  debate_id = new FormControl('', Validators.required);

  constructor(
    public service: PostService,
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
    this.post = new Post(
      this.form.value.title,
      this.form.value.text,
      this.form.value.user_id,
      this.form.value.debate_id
      );
    this.service.createPost(this.post).subscribe(
      data => {
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
  }
}
