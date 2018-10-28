import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap, Router } from '@angular/router';
import { DebateService } from 'src/app/services/debate/debate.service';
import { Debate } from '../debate';
import { switchMap } from 'rxjs/operators';
import { Post } from 'src/app/components/post/post';
import { PostService } from 'src/app/services/post/post.service';

@Component({
  selector: 'app-get-debate',
  templateUrl: './get-debate.component.html',
  styleUrls: ['./get-debate.component.css']
})
export class GetDebateComponent implements OnInit {
  private debate: Debate;
  private post_ids: number[];
  private posts: Post[];

  constructor(
    private route: ActivatedRoute,
    private service: DebateService,
    private router: Router,
    private post_service: PostService
    ) {
      this.debate = new Debate('', '', '', '', '', []);
     }

  ngOnInit() {
    this.route.paramMap.pipe(
      switchMap((params: ParamMap) =>
        this.service.getDebate(params.get('id'))
      )
    )
    .subscribe(
      debate => {
        this.debate = debate;
        console.log(this.debate);
        this.post_ids = this.debate.posts;
        console.log(this.post_ids);
      },
      error => {
        console.log(error);
        if (error.status === 404) {
          this.router.navigate(['404']);
        }
      });
  }
}
