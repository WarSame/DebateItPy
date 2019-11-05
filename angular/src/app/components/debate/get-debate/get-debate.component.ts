import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap, Router } from '@angular/router';
import { DebateService } from 'src/app/services/debate/debate.service';
import { Debate } from '../debate';
import { switchMap } from 'rxjs/operators';
import { Argument } from 'src/app/components/argument/argument';
import { ArgumentService } from 'src/app/services/argument/argument.service';

@Component({
  selector: 'app-get-debate',
  templateUrl: './get-debate.component.html',
  styleUrls: ['./get-debate.component.css']
})
export class GetDebateComponent implements OnInit {
  private debate: Debate;
  private post_ids: number[];
  private arguments: Argument[];

  constructor(
    private route: ActivatedRoute,
    private service: DebateService,
    private router: Router,
    private argument_service: ArgumentService
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
      },
      error => {
        console.log(error);
        if (error.status === 404) {
          this.router.navigate(['404']);
        }
      });
  }
}
