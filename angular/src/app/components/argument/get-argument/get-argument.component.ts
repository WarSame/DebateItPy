import { Component, OnInit } from '@angular/core';
import { ArgumentService } from 'src/app/services/argument/argument.service';

import { ActivatedRoute, ParamMap, Router } from '@angular/router';

import { switchMap } from 'rxjs/operators';
import { Argument } from '../argument';

@Component({
  selector: 'app-argument',
  templateUrl: './get-argument.component.html',
  styleUrls: ['./get-argument.component.css']
})
export class GetArgumentComponent implements OnInit {
  private argument: Argument;

  constructor(
    private service: ArgumentService,
    private route: ActivatedRoute,
    private router: Router
    ) {
      this.argument = new Argument('', '', '', '');
  }

  ngOnInit() {
    this.route.paramMap.pipe(
      switchMap((params: ParamMap) =>
        this.service.getArgument(params.get('id'))
      )
    )
    .subscribe(
      argument => {
        this.argument = argument;
        console.log(argument);
      },
      error => {
        console.log(error);
        this.router.navigate(['404']);
      });
  }

}
