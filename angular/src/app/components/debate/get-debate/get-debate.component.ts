import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap, Router } from '@angular/router';
import { DebateService } from 'src/app/services/debate/debate.service';
import { Debate } from '../debate';
import { switchMap } from 'rxjs/operators';
import { Argument } from '../../argument/argument';

const arg1 = new Argument('sometitle', 'somecontent', '1', '1');

@Component({
  selector: 'app-get-debate',
  templateUrl: './get-debate.component.html',
  styleUrls: ['./get-debate.component.css']
})
export class GetDebateComponent implements OnInit {
  private debate: Debate;


  constructor(
    private route: ActivatedRoute,
    private service: DebateService,
    private router: Router
    ) {
      this.debate = new Debate('', '', '', '', [arg1]);
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
        this.debate.arg_list = [arg1];
      },
      error => {
        console.log(error);
        if (error.status === 404) {
          this.router.navigate(['404']);
        }
      });
  }
}
