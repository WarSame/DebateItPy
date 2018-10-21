import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { DebateService } from 'src/app/services/debate/debate.service';
import { Debate } from '../debate';
import { switchMap } from 'rxjs/operators';

@Component({
  selector: 'app-get-debate',
  templateUrl: './get-debate.component.html',
  styleUrls: ['./get-debate.component.css']
})
export class GetDebateComponent implements OnInit {
  private route: ActivatedRoute;
  private service: DebateService;
  private debate: Debate;

  constructor(
    route: ActivatedRoute,
    service: DebateService
    ) {
      this.service = service;
      this.route = route;
      this.debate = new Debate('', '', '', '', '');
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
      },
      error => {
        console.log(error);
      });
  }
}
