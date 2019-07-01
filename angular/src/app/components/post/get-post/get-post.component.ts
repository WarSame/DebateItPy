import { Component, OnInit } from '@angular/core';
import { PostService } from 'src/app/services/post/post.service';

import { ActivatedRoute, ParamMap, Router } from '@angular/router';

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
    private service: PostService,
    private route: ActivatedRoute,
    private router: Router
    ) {
      this.post = new Post('', '', '', '');
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
        console.log(post);
      },
      error => {
        console.log(error);
        this.router.navigate(['404']);
      });
  }

}
