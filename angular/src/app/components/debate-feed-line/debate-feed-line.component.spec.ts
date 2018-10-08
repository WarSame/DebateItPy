import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DebateFeedLineComponent } from './debate-feed-line.component';

describe('DebateFeedLineComponent', () => {
  let component: DebateFeedLineComponent;
  let fixture: ComponentFixture<DebateFeedLineComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DebateFeedLineComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DebateFeedLineComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
