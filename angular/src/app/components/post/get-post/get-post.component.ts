import { Component, OnInit } from '@angular/core';
import { PostService } from 'src/app/services/post/post.service';

import { ActivatedRoute, ParamMap } from '@angular/router';

import { switchMap } from 'rxjs/operators';
import { Post } from '../post';

@Component({
  selector: 'app-post',
  templateUrl: './get-post.component.html',
  styleUrls: ['./get-post.component.css']
})
export class GetPostComponent implements OnInit {
  private post: Post;

  constructor(
    public service: PostService,
    private route: ActivatedRoute
    ) {
    this.service = service;
  }

  ngOnInit() {
    this.route.paramMap.pipe(
      switchMap((params: ParamMap) =>
        this.service.getPost(params.get('id'))
      )
    )
    .subscribe(
      post => {
        this.post = post;
      },
      error => {
        console.log(error);
      });
  }

}
