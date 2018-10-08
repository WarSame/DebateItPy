import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TopTargetedFeedComponent } from './top-targeted-feed.component';

describe('TopTargetedFeedComponent', () => {
  let component: TopTargetedFeedComponent;
  let fixture: ComponentFixture<TopTargetedFeedComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TopTargetedFeedComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TopTargetedFeedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
