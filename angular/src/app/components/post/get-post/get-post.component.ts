import { Component, OnInit } from '@angular/core';
import { PostService } from 'src/app/services/post/post.service';

import { Router, ActivatedRoute, ParamMap } from '@angular/router';

import { switchMap } from 'rxjs/operators';

@Component({
  selector: 'app-post',
  templateUrl: './get-post.component.html',
  styleUrls: ['./get-post.component.css']
})
export class GetPostComponent implements OnInit {
  private post;

  constructor(
    public service: PostService,
    private route: ActivatedRoute,
    private router: Router
    ) {
    this.service = service;
  }

  ngOnInit() {
    this.post = this.route.paramMap.pipe(
      switchMap((params: ParamMap) =>
        this.service.getPost(params.get('id'))
      )
    )
    .subscribe(
      data => {
        this.post = data;
      },
      error => {
        console.log(error);
      });
  }

}
